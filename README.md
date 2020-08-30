# guess-the-doodle
<img src="https://quickdraw.withgoogle.com/static/shareimg.png"/>
Based on google's quick draw game

# To run the project

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
