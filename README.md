# guess-the-doodle
<img src="https://quickdraw.withgoogle.com/static/shareimg.png"/>
Based on google's quick draw game

# To run the project

You'll be needing npm and conda for this project to work on your local machine.

## Part 0 - Clone the repo to your local machine
1) Clone the repo in your local machine
2) Set up the enviroment:
  2.1) Install live-server package from npm. (npm install -g live-server)
  2.2) In folder quick-draw-server you will find enviroment.yml file needed to set up the conda environment.
  2.3) Run conda env create -f environment.yml from the terminal in this folder.
  2.4) After the above command completes a new environment named quickdrawwnv will be created in conda.
  2.5) Switch to this environment using: conda activate quickdrawwnv
3) After the environment is set up from folder quick_draw_server run: python app.py from the terminal.
4) From folder quickDraw inside the terminal run live-server. This will open a new tab in your browser.
5) However the project requires a model.h5 file and classes.npy which need to be created and the steps are provided below.

## Part 1 - Collect Data
1) Open collect_quick_draw_data.ipynb in google colab.
2) Run cells one by one, you'll be prompted to allow google colab to access your google drive provide authorization code as instructed.
3) Once you connect GDrive with colab the script will make a folder named quick_draw_data in your GDrive.
4) All data will be downloaded in this folder once the script completes.

## Part 2 - Train the model
1) Open quick_draw_cnn.ipynb in google colab.
2) Once again you will be prompted to connect GDrive with Google colab (Make sure you login with the same account you did previously since this script needs access to the quick_draw_data folder.
3) Keep running the cells one by one, the data in loaded and model will be trained. (This might take a while)
4) When the script completes and succeeds a model.h5 file will be saved in your GDrive main folder.
5) Download this model to your local machine.
6) Also a numpy array will be saved in the main GDrive folder named classes.npy
7) Download this list to your local machine as well.

## Part 3 - Add model.h5 and classes.npy to quick-draw-server
1) Once you have model.h5 and classes.npy add them to the folder quick-draw-server.
2) Start the server using 'python app.py'
3) From folder quickDraw run 'live-server' to launch a new tab in your browser.
4) Start drawing in the canvas and you would see the models output.
