
## Gitpod Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.


## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.



## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.


## Hypothesis and how to validate?
* It is excpected that the leaf with mildew will be detected through its destinct spots caused by the mildew deasese.
* The validation will be made thorugh comparision with a healthy leaf(Image study)


## The rationale to map the business requirements to the Data Visualisations and ML tasks

### Business Requirement 1: Data Visualization

* We will display the "mean" and "standard deviation" images for healthy and mildew containing leaf's.
* We will display the difference between an average healthy leaf and an average mildew containing leaf.
* We will display a image montage for either healthy or mildew containing leaf.

### Business Requirement 2: Classification

* we want to predict if an leaf is infected with mildew or not.
* We want to build a binary classifier using Neural networks and generate reports.


## ML Business Case

### MildewCLF

* We want a ML model to predict if a leaf is infected with mildew or not, based on historical image data. It is a supervised model, a 2-class, single-label, classification model.
* Our ideal outcome is provide the farm team a faster and reliable diagnostic if a given leaf/tree is infected or not with mildew.
* The model success metrics are
Accuracy of 97% or above on the test set.
* The model output is defined as a flag, indicating if the leaf has mildew or not and the associated probability of being infected or not. The farm staff will do collect the lleafs as usual and upload the picture to the App. The prediction is made on the fly (not in batches).
* Heuristics: The current diagnostic needs an experienced staff and detailed inspection to distinguish mildew containing or healthy leafs. A leaf sample is collected, mixed with a reagent and examined under the microscope. Visual criteria are used to detect mildew. It leaves room to produce inaccurate diagnostics due to human errors And takes alot of time. 
* The training data to fit the model come from Code institute and was found the kaggle Website. This dataset contains about 4208 images. We have extracted a subset of 4208 images from this dataset and saved it to kaggle dataset directory for quicker model training.
Train data - target: infected or not; features: all images

FIXING THIS AND THE UPPER IN THE PROJECT
## Dashboard Design
* Page 1: Quick Project Summary
Quick project summary
General Information
Mildew is an fungus that can infect the leafs of the cherry tree.
A leaf from the cherry tree is collected. Visual criteria are used to detect mildew fungus.
The mildew fungus is devistating to the cherry tree farmers and takes alot of time for the farm workers to detect and handle
Project Dataset
The dataset is containing 4208 pictures and is taken from [kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves/code)
Business requirements
The client is interested in a study to differentiate between a Mildew contained leaf and a healthy leaf.
The client is interested in telling whether a given leaf(tree) contains mildew or not.
Page 2: leaves visualizer
It will answer business requirement 1
Checkbox 1 - Difference between average and variability image
Checkbox 2 - Differences between average mildew containing and average healthy leaf
Checkbox 3 - Image Montage
Page 3: Mildew Detector
Business requirement 2 information - "The client is interested to tell whether a given leaf contains Mildew fungus or not."
Link to download a set of mildew contained and healthy leaf images for live prediction.
User Interface with a file uploader widget. The user should upload multiple mildew leaf image. It will display the image and a prediction statement, indicating if the leaf is containing mildew or not and the probability associated with this statement.
Table with image name and prediction results.
Download button to download table.
Page 4: Project Hypothesis and Validation
Bloack for each project hypothesis, describe the conclusion and how you validated.
Page 5: ML Performance Metrics
Label Frequencies for Train, Validation and Test Sets
Model History - Accuracy and Losses
Model evaluation result

## Unfixed Bugs
* Grayscale imageset
    * I decided not to use the grayscale image set because of the good results from the RGB image set.
    * The grayscale image set and model also made the workspace to heavy in terms of memory.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.


## Main Data Analysis and Machine Learning Libraries
* kaggle
    * Kaggle is used to fetch/import the dataset for this project

* PIL
    * PIL is used to turn the pictures into grayscale imageset (Though not used in the final deployment)

* OS
    * Is used to fetch/get/create files and paths throughout the project

* Joblib
    * Used to save files and images thorughtout the project

* Random
    * Random is used to shuffle and create "random" instances throughout the project 

* seaborn
    * Is used to create plots/charts etc

* matplotlib.pyplot
    * Also used to create plots etc

* tensorflow
    * keras.preprocessing is used to load the picturen into array
    * tensorflow.keras.preprocessing.image is used for agmentation
    * tensorflow.keras.models is used to determine the model type
    * tensorflow.keras.layers is used to determine the layers inside the model
    * tensorflow.keras.initializer is used for the kernal initializer in the model
    * tensorflow.keras.callbacks is used for earlystopping when training to reduce risk of overfitting

* numpy
    * Numpy provides ability to load multidimensional arrays and other tools to help finding items inside arrays

* itertools
    * Is used to iterate through images in dataset

* Pandas
    * Is used to fetch model history
 


## Credits 

### Media credits

- The dataset is taken from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves/code) 

### Content 

- The base template for this project was taken from Code Institute
- Much of the work is inpsired of the Malaria detection project provided by Code Insitute.

- Articles that have inspired this project.
    - [Medium](https://medium.com/zero-equals-false/early-stopping-to-avoid-overfitting-in-neural-network-keras-b68c96ed05d9)
    - [Geeksforgeeks](https://www.geeksforgeeks.org/choose-optimal-number-of-epochs-to-train-a-neural-network-in-keras/)
    - [Github](https://github.com/grajpal123/Emergency_Non-Emergency_Vehicle_Image_Classification/blob/main/Model%20Checkpointing%20in%20Keras.ipynb)
    - [Numpy ninja](https://www.numpyninja.com/post/weight-initialization-techniques)

