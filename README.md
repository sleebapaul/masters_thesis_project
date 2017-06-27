# M.Tech-Thesis-Project
-----------------------

M. Tech. Thesis Project on " Detection and Identification of Hybrid Distribution System Using Wavelet Transform and Artificial Neural Networks" is documented here.

### Abstract
--------------
In this thesis, Islanding and Power Quality(PQ) Issues in Hybrid Distributed Generation (DG) System consists of Photovoltaic(PV) system and Wind Power Plant connected to grid through a Point of Common Coupling(PCC), are detected and classified, using Wavelet Transform and Artificial Neural Networks. Wavelet Transform indices are extracted from the Negative Sequence component of the voltage signal at PCC to detect the disturbances. A feature vector is modeled with WT indices and loading of DG system to train Artificial Neural Network. . The proposed method is compared with a conventional method. The results demonstrate the advantages of Wavelet over conventional method in detection and classification of disturbances in the system and robustness in application of Machine Learning (ML) Classifier. The trained ANN is deployed as a Web Service using Microsoft Azure Machine Learning Studio. It enhances the implementation feasibility of proposed method.

###  Hybrid Distributed Generation
----------------------------------
![Alt text](M.Tech-Thesis-Project/files/hybrid_system.png "Hybrid DG System")

### Simulation Diagram in MATLAB Simulink
-----------------------------------------
![Alt text](https://github.com/sleebapaul/sentiment_analysis_take_off_movie/blob/master/movie_poster.jpg "Simulation Diagram")

### Work Flow
-------------

1. Simulate the `simulation_diagram.mdl` using `script_get_training_data.m` for following situations and collect the training data for ANN
    - Grid Connected (Normal)
    - Islanding
    - L-L Fault 
    - L-G Fault
    - Nonlinear Load Switch
2. From negative sequence voltage at PCC during these events, extract the following features
    - Standard Deviation of detail coefficients of Wavelet Transform of negative sequence voltage signal at level 3 (`SD3`)
    - Standard Deviation of detail coefficients of Wavelet Transform of negative sequence voltage signal at level 4 (`SD4`)
    - Energy content of detail coefficients of Wavelet Transform of negative sequence voltage signal at level 3 (`E3`)
    - Energy content of detail coefficients of Wavelet Transform of negative sequence voltage signal at level 4 (`E4`)
3. ANN is trained at `Microsoft Azure Machine Learning Studio` by uploading the training data to cloud as a `.csv` file
    - Train the ANN locally using `main_program_ann.m` from `ann_code` folder for testing purpose
4. Sample training data would be as follows

| Loading | SD4      | SD3      | E4       | E3       | Label                  |
|---------|----------|----------|----------|----------|------------------------|
| 0.91    | 0.00016  | 0.000123 | 0.001321 | 0.001398 | Normal                 |
| 1.155   | 0.000165 | 0.000105 | 0.001364 | 0.001199 | Normal                 |
| 1.05    | 0.046179 | 0.035238 | 0.381349 | 0.403484 | Islanding              |
| 1.12    | 0.046168 | 0.041096 | 0.38108  | 0.471473 | Islanding              |
| 0.98    | 0.011971 | 0.004943 | 0.098714 | 0.056379 | L-G Fault              |
| 1.085   | 0.011999 | 0.004949 | 0.098944 | 0.056448 | L-G Fault              |
| 1.365   | 0.029071 | 0.009113 | 0.239756 | 0.10396  | L-L Fault              |
| 1.715   | 0.028943 | 0.009125 | 0.238704 | 0.1041   | L-L Fault              |
| 1.225   | 0.025061 | 0.012793 | 0.20666  | 0.146597 | Non-Linear Load Switch |
| 1.435   | 0.025036 | 0.012789 | 0.206452 | 0.146566 | Non-Linear Load Switch |

3. Using Python GUI, consume the web service as a  `POST` request to predict the states of the system (as mentioned above)
    - Python GUI can be with `gui_and_azure_api_consumption.py`

### Microsoft Azure Web Service Architecture
--------------------------------------------
![Alt text](https://github.com/sleebapaul/sentiment_analysis_take_off_movie/blob/master/experiment.png "ML Experiment")

![Alt text](https://github.com/sleebapaul/sentiment_analysis_take_off_movie/blob/master/prediction.png "Web Service")

### Python GUI
--------------

![Alt text](https://github.com/sleebapaul/sentiment_analysis_take_off_movie/blob/master/pic1.png "Before")

![Alt text](https://github.com/sleebapaul/sentiment_analysis_take_off_movie/blob/master/pic2.png "after")





