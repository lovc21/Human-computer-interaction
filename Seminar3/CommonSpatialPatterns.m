
subject = 'S001';
records = [];

for i = 1:14  
    records{end+1} = strcat(subject, 'R', num2str(i, '%02d'), '.edf');
end
disp(records);

t1 = {};
t2 = {};

baseDir = 'C:\Users\Jakob\Seminar1\S001';

for i = 1:length(records)
    fileName = records{i};
    filePath = fullfile(baseDir, fileName);
  
    disp(filePath)

    disp(['Processing file: ', filePath]);
    % Read EEG data from an EDF file 1:64 specifies the channels to be read
    [eeg, fs, ts] = rdsamp(filePath, 1:64);

    disp('rdsamp done')

    %Plotting the EEG data
    figure; 
    plot(ts, eeg); 
    title('EEG Data'); 
    xlabel('Time (s)'); 
    ylabel('EEG Signal'); 
    
    % Transposing the EEG data matrix
    eeg = eeg.';
    
    % Categorize and store intervals of an EEG signal into three different categories: T0, T1, and T2.

    [T0, T1, T2] = getIntervals(filePath, 'event', fs, size(eeg, 2));
    disp('getIntervals done')

    for j=1:size(T1,1)
        t1{end+1} = eeg(:,T1(j,1):T1(j,2));
    end
    
    for j=1:size(T1,1)
        t2{end+1} = eeg(:,T1(j,1):T1(j,2));
    end
end


t1dat0 = cell2mat(t1(1:2));
t2dat0 = cell2mat(t2(1:2));

% Applying CSP
W = f_CSP(t1dat0, t2dat0);


% Plotting the CSP components
figure;
plot(W);
title('CSP Components');
xlabel('Components');
ylabel('Amplitude');

% Applying CSP to the data
S11 = W * t1dat0;
S21 = W * t2dat0;

% Plotting transformed signals using CSP
figure;
subplot(2,1,1);
plot(S11');
title('Transformed Signal T1 using CSP');
xlabel('Samples');
ylabel('Amplitude');
subplot(2,1,2);
plot(S21');
title('Transformed Signal T2 using CSP');
xlabel('Samples');
ylabel('Amplitude');

%filter definition
f = [0 8 8 13 13 fs/2]/(fs/2); 
a = [0 0 1 1 0 0 ]; 
n= 35; 
b = firls(n, f, a);

% Removing the first pair of activities from the sets
t1(1) = [];
t2(1) = [];

% Initializing feature matrices
feature1 = zeros(size(t1, 2), 2);
feature2 = zeros(size(t2, 2), 2);

% Feature extraction for each activity in t1
for i = 1:size(t1, 2)
    tmp = (W * cell2mat(t1(i)));
    tmp = [tmp(1, :).', tmp(end, :).'].'; % Selecting first and last rows
    tmp = filter(b, 1, tmp); % Applying bandpass filter
    feature1(i, :) = [log(var(tmp(1, :))), log(var(tmp(2, :)))];
end

% Feature extraction for each activity in t2
for i = 1:size(t2, 2)
    tmp = (W * cell2mat(t2(i)));
    tmp = [tmp(1, :).', tmp(end, :).'].'; % Selecting first and last rows
    tmp = filter(b, 1, tmp); % Applying bandpass filter
    feature2(i, :) = [log(var(tmp(1, :))), log(var(tmp(2, :)))];
end

% Plotting the features
figure;
scatter(feature1(:,1), feature1(:,2), 'b');
hold on;
scatter(feature2(:,1), feature2(:,2), 'r');
xlabel('Feature 1');
ylabel('Feature 2');
legend('t1', 't2');
title('Feature Scatter Plot');
hold off;

featVFile = strcat('S001', 'featureVectors.txt');
classFile = strcat('S001', 'referenceClass.txt');

fvf = fopen(featVFile, 'wt');
rcf = fopen(classFile, 'wt');

 for i=1:size(feature1,1)
   fprintf(fvf, '%.8f %.8f\n', feature1(i,1), feature1(i,2));
   fprintf(rcf, 'T1\n');
 end

for i=1:size(feature2,1)
   fprintf(fvf, '%.8f %.8f\n', feature2(i,1), feature2(i,2));
   fprintf(rcf, 'T2\n');
end

fclose(fvf);
fclose(rcf);

doClassification('S001featureVectors.txt','S001referenceClass.txt',{1,1},10, 50, 0)

function [T0, T1, T2] = getIntervals(recName, annot, fs, len)
    T0=[];
    T1=[];
    T2=[];
    [a, ~, ~, ~, ~, cmt] = rdann(recName, annot);
    cmt=string(cmt);
    for idx=1:length(cmt)
        splt = split(cmt(idx),' ');
        dur = str2double(splt(3))*fs;
        intEnd = a(idx)+dur-1;
        if (idx<length(a))
            intEnd=min(a(idx+1)-1, intEnd);
        else
            intEnd=min(len, intEnd);
        end
        if (splt(1)=="T0")
            T0=[T0; a(idx) intEnd];
        elseif (splt(1)=="T1")
            T1=[T1; a(idx) intEnd];
        elseif (splt(1)=='T2')
            T2=[T2; a(idx) intEnd];
        end
    end
end


function [result] = f_CSP(varargin)
% This code is for calulating the projection matrix for CSP 
% Haider Raza, Intelligent System Research Center, University of Ulster, Northern Ireland, UK.
%     Raza-H@email.ulster.ac.uk
%     Date: 03-Oct-2014
% Input:
%             
%       left:  left hand data
%       right: right hand data
% 
% Output:
%        left: Left hand data
%        right: right hand data    

    if (nargin ~= 2)
        disp('Must have 2 classes for CSP!')
    end
    
    Rsum=0;
    %finding the covariance of each class and composite covariance
    for i = 1:nargin 
        %mean here?
        R{i} = ((varargin{i}*varargin{i}')/trace(varargin{i}*varargin{i}'));%instantiate me before the loop!
        %Ramoser equation (2)
        Rsum=Rsum+R{i};
    end
   
    %   Find Eigenvalues and Eigenvectors of RC
    %   Sort eigenvalues in descending order
    [EVecsum,EValsum] = eig(Rsum);
    [EValsum,ind] = sort(diag(EValsum),'descend');
    EVecsum = EVecsum(:,ind);
    
    %   Find Whitening Transformation Matrix - Ramoser Equation (3)
        W = sqrt(inv(diag(EValsum))) * EVecsum';
    
    
    for k = 1:nargin
        S{k} = W * R{k} * W'; %       Whiten Data Using Whiting Transform - Ramoser Equation (4)
    end
   
    %generalized eigenvectors/values
    [B,D] = eig(S{1},S{2});
    % Simultanous diagonalization
			% Should be equivalent to [B,D]=eig(S{1});
    
    [D,ind]=sort(diag(D));B=B(:,ind);
    
    %Resulting Projection Matrix-these are the spatial filter coefficients
    result = B'*W;

end