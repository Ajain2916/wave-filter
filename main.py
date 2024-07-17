# import numpy as np
# import pandas as pd
# import scipy.signal as signal
# import matplotlib.pyplot as plt
# import os

# def list_csv_files(directory):
#     """List all .csv files in the given directory."""
#     return [f for f in os.listdir(directory) if f.endswith('.csv')]

# def load_csv_file(filepath):
#     """Load wave data from a .csv file."""
#     df = pd.read_csv(filepath)
#     df.columns = df.columns.str.strip()  # Strip any leading/trailing spaces from headers
#     print("CSV DataFrame Headers:", df.columns.tolist())  # Debugging step
#     print(df.head())  # Debugging step
#     data = df['Amplitude'].values
#     samplerate = df['SampleRate'].iloc[0]
#     return data, samplerate

# def plot_wave(data, samplerate, title="Waveform"):
#     """Plot the waveform of the audio signal."""
#     time = np.arange(len(data)) / samplerate
#     plt.figure()
#     plt.plot(time, data)
#     plt.title(title)
#     plt.xlabel('Time [s]')
#     plt.ylabel('Amplitude')
#     plt.show()

# def apply_filter(data, samplerate, filter_type, cutoff, filter_order=3):
#     """Apply a filter to the audio signal."""
#     nyquist = 0.5 * samplerate
#     norm_cutoff = np.array(cutoff) / nyquist
#     if filter_type == 'lowpass':
#         b, a = signal.butter(filter_order, norm_cutoff, btype='low')
#     elif filter_type == 'highpass':
#         b, a = signal.butter(filter_order, norm_cutoff, btype='high')
#     elif filter_type == 'bandpass':
#         b, a = signal.butter(filter_order, norm_cutoff, btype='band')
#     filtered_data = signal.filtfilt(b, a, data, padlen=min(len(data)-1, 3*(max(len(b), len(a))-1)))
#     return filtered_data

# def main():
#     # Directory containing CSV files
#     csv_directory = 'data'
    
#     # List available CSV files
#     csv_files = list_csv_files(csv_directory)
#     print("Available CSV files:")
#     for i, file in enumerate(csv_files):
#         print(f"{i+1}. {file}")
    
#     # Get user input to select CSV file
#     file_index = int(input("Select the CSV file index: ")) - 1
#     selected_file = csv_files[file_index]
#     data, samplerate = load_csv_file(os.path.join(csv_directory, selected_file))
    
#     # Plot the original wave
#     plot_wave(data, samplerate, title="Original Waveform")
    
#     # Get user input for filter type and cutoff frequency
#     filter_type = input("Enter filter type (lowpass, highpass, bandpass): ")
#     if filter_type == 'bandpass':
#         low_cutoff = float(input("Enter low cutoff frequency (Hz): "))
#         high_cutoff = float(input("Enter high cutoff frequency (Hz): "))
#         cutoff = [low_cutoff, high_cutoff]
#     else:
#         cutoff = float(input(f"Enter cutoff frequency (Hz) for {filter_type}: "))
    
#     # Apply the selected filter
#     filtered_data = apply_filter(data, samplerate, filter_type, cutoff)
    
#     # Plot the filtered wave
#     plot_wave(filtered_data, samplerate, title="Filtered Waveform")

# if __name__ == "__main__":
#     main()
import numpy as np
import pandas as pd
import scipy.signal as signal
import matplotlib.pyplot as plt
import os

def list_csv_files(directory):
    """List all .csv files in the given directory."""
    return [f for f in os.listdir(directory) if f.endswith('.csv')]

def load_csv_file(filepath):
    """Load wave data from a .csv file."""
    df = pd.read_csv(filepath)
    df.columns = df.columns.str.strip()  # Strip any leading/trailing spaces from headers
    print("CSV DataFrame Headers:", df.columns.tolist())  # Debugging step
    print(df.head())  # Debugging step
    data = df['Amplitude'].values
    samplerate = df['SampleRate'].iloc[0]
    return data, samplerate

def plot_wave(data, samplerate, title="Waveform"):
    """Plot the waveform of the audio signal."""
    time = np.arange(len(data)) / samplerate
    plt.figure()
    plt.plot(time, data)
    plt.title(title)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.show()

def apply_filter(data, samplerate, filter_type, cutoff, filter_order=3):
    """Apply a filter to the audio signal."""
    nyquist = 0.5 * samplerate
    norm_cutoff = np.array(cutoff) / nyquist
    if filter_type == 'lowpass':
        b, a = signal.butter(filter_order, norm_cutoff, btype='low')
    elif filter_type == 'highpass':
        b, a = signal.butter(filter_order, norm_cutoff, btype='high')
    elif filter_type == 'bandpass':
        b, a = signal.butter(filter_order, norm_cutoff, btype='band')
    filtered_data = signal.filtfilt(b, a, data, padlen=min(len(data)-1, 3*(max(len(b), len(a))-1)))
    return filtered_data

def main():
    # Directory containing CSV files
    csv_directory = 'data'
    
    # List available CSV files
    csv_files = list_csv_files(csv_directory)
    print("Available CSV files:")
    for i, file in enumerate(csv_files):
        print(f"{i+1}. {file}")
    
    # Get user input to select CSV file
    file_index = int(input("Select the CSV file index: ")) - 1
    selected_file = csv_files[file_index]
    data, samplerate = load_csv_file(os.path.join(csv_directory, selected_file))
    
    # Plot the original wave
    plot_wave(data, samplerate, title="Original Waveform")
    
    # Get user input for filter type and cutoff frequency
    filter_type = input("Enter filter type (lowpass, highpass, bandpass): ")
    if filter_type == 'bandpass':
        low_cutoff = float(input("Enter low cutoff frequency (Hz): "))
        high_cutoff = float(input("Enter high cutoff frequency (Hz): "))
        cutoff = [low_cutoff, high_cutoff]
    else:
        cutoff = float(input(f"Enter cutoff frequency (Hz) for {filter_type}: "))
    
    # Get user input for amplitude range
    min_amplitude = float(input("Enter minimum amplitude for filtering: "))
    max_amplitude = float(input("Enter maximum amplitude for filtering: "))
    
    for amplitude in np.linspace(min_amplitude, max_amplitude, num=5):
        print(f"Filtering with amplitude: {amplitude}")
        # Apply the selected filter
        filtered_data = apply_filter(data * amplitude, samplerate, filter_type, cutoff)
        
        # Plot the filtered wave
        plot_wave(filtered_data, samplerate, title=f"Filtered Waveform with amplitude {amplitude}")

if __name__ == "__main__":
    main()
