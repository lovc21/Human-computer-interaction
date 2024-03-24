iterationCount = 0;  
maxIterations = 10;  
rng(1);

while maxIterations > iterationCount

    fprintf('Welcome to the removal of eye artifacts script \n')
    fprintf('Please have the edf signals in the folder where are you going to be executing the script(i.e. mydir-> S001R03.edf and EliminatingOcularArtifactsUsingANK.m) \n')
    fprintf('If you want to exit the script just klit ctrl +c\n')
    mapInput = input('Enter the data for removal of eye artifacts (example:S001R03.edf):','s');
    [eeg, fs, ts] = rdsamp(mapInput, 1:64);
    
    %Bandpass filter the data and EEG signals
    order =4;  
    lowcut = 1; 
    highcut = 30;

    %uporabi funkcijo filterfilter
    [b, a] = butter(order, [lowcut highcut] / (fs / 2), 'bandpass');
    eegSignals = filtfilt(b, a, eeg);
    
    eegSignalsTranspose = eegSignals';

    figure('Name', 'Filterd Original EEG Signals');
    plot(eegSignalsTranspose(1,:));
    title('Filterd Original EEG Signals');
    xlabel('Time');
    ylabel('Amplitude');

    eegTranspose = eeg';
    figure('Name', 'Not filterd Original EEG Signals');
    plot(eegTranspose(1,:));
    title('Not Filterd Original EEG Signals');
    xlabel('Time');
    ylabel('Amplitude');

    drawnow;
    % Transpose eeg
    eeg = eeg';

    % Transpose eegSignals
    eegSignals = eegSignals';

    %Apply FastICA
    [icasig, A, W] = fastica(eeg);
    
    numComponents = size(icasig, 1);
    numRows = ceil(sqrt(numComponents));
    numCols = ceil(numComponents / numRows);
    
    %Plot signals 
    figure('Name', 'ICA Components');
    for i = 1:numComponents
        subplot(numRows, numCols, i);
        plot(icasig(i, :));
        title(['Independent Component ' num2str(i)]);
    end
  
    blinkComponentsStr = input('Enter components that represent blinks (e.g., [1 3 5]): ','s');
    
    blinkComponents = str2num(blinkComponentsStr);
    disp(blinkComponents)

    if ~isempty(blinkComponents) && all(blinkComponents <= numComponents)
        
        icasig(blinkComponents, :) = 0;

        cleanedSignals = A * icasig;

        %Plot the signals
        figure('Name', 'Cleaned EEG Signals vs Original');
        plot(cleanedSignals(1,:));
        hold on;
        plot(eeg(1,:))
        title('Cleaned EEG Signals vs Original');
        xlabel('Time');
        ylabel('Amplitude');

        figure('Name', 'Cleaned EEG Signals');
        plot(cleanedSignals(1,:));
        title('Cleaned EEG Signals');
        xlabel('Time');
        ylabel('Amplitude');

        fprintf('eye artifacts are remov from %1$s \n',mapInput);
    else
        fprintf('Invalid component numbers entered.\n');
    end

end