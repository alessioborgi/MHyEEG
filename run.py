import os
import subprocess


seeds = [1,2]
models = ['HyperNet']

for model in models:
    for seed in seeds:
        subprocess.run(['python', 'main.py',
                        '--train_file_path', 'G:/.shortcut-targets-by-id/1a4C1sZZVLYPHnSjH1T4GtC0Fr5t7E_bb/MAHNOB Dataset/hci-tagging-database/Torch_datasets/Train_Data_full-eye-GSR-NO-BASE_augm-scale+noise_m30_SNR5_Vlnc.pt',
                        '--test_file_path', 'G:/.shortcut-targets-by-id/1a4C1sZZVLYPHnSjH1T4GtC0Fr5t7E_bb/MAHNOB Dataset/hci-tagging-database/Torch_datasets/Test_size-0.2_Data_full-eye-GSR-NO-BASE_augm-scale+noise_m30_SNR5_Vlnc.pt',
                        '--dropout_rate', '0.5',
                        '--model', model,
                        '--seed', str(seed)])

for model in models:
    for seed in seeds:
        subprocess.run(['python', 'main.py',
                        '--train_file_path', 'G:/.shortcut-targets-by-id/1a4C1sZZVLYPHnSjH1T4GtC0Fr5t7E_bb/MAHNOB Dataset/hci-tagging-database/Torch_datasets/Train_Data_full-eye-GSR-NO-BASE_augm-scale+noise_m30_SNR5_Arsl.pt',
                        '--test_file_path', 'G:/.shortcut-targets-by-id/1a4C1sZZVLYPHnSjH1T4GtC0Fr5t7E_bb/MAHNOB Dataset/hci-tagging-database/Torch_datasets/Test_size-0.2_Data_full-eye-GSR-NO-BASE_augm-scale+noise_m30_SNR5_Arsl.pt',
                        '--dropout_rate', '0.5',
                        '--model', model,
                        '--seed', str(seed)])

# models = ['HyperFuseNet']

# for model in models:
#     subprocess.run(['python', 'main.py',
#                     '--train_file_path', 'G:/.shortcut-targets-by-id/1a4C1sZZVLYPHnSjH1T4GtC0Fr5t7E_bb/MAHNOB Dataset/hci-tagging-database/Torch_datasets/Train_Data_full-eye-GSR-NO-BASE_augm-scale+noise_m30_SNR5_Vlnc.pt',
#                     '--test_file_path', 'G:/.shortcut-targets-by-id/1a4C1sZZVLYPHnSjH1T4GtC0Fr5t7E_bb/MAHNOB Dataset/hci-tagging-database/Torch_datasets/Test_size-0.2_Data_full-eye-GSR-NO-BASE_augm-scale+noise_m30_SNR5_Vlnc.pt',
#                     '--dropout_rate', '0.2118',
#                     '--epochs', '60',
#                     '--min_mom', '0.8314',
#                     '--max_mom', '0.9735',
#                     '--max_lr', '0.002489',
#                     '--patience', '20',
#                     '--model', model])