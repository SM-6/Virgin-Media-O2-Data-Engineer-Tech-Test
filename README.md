# Virgin-Media-O2-Data-Engineer-Tech-Test

**Project Overview**

This project is for the Virgin Media O2 Data Engineering tech test.

**Description**

In accordance with the provided instructions, I've developed a batch pipeline capable of reading a CSV file, executing various data transformation processes, and generating a new file in the designated output location. For Task 1, I created a Jupyter Notebook for each section, which can be found in the src folder labeled batch_job_task1.ipynb. The complete end-to-end solution for Task 2 is encapsulated in the file named composite_transform_pipeline_task2.py, also available in the src folder of this repository.

## Instructions

To execute the pipeline on macOS, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/SM-6/Virgin-Media-O2-Data-Engineer-Tech-Test.git
   ```

2. Navigate to the repository directory:
   ```bash
   cd Virgin-Media-O2-Data-Engineer-Tech-Test 
   ```

3. Set up a virtual environment:
   ```bash
   python3 -m venv venv 
   ```

4. Activate the virtual environment:
   ```bash
   source venv/bin/activate 
   ```

5. Install the required dependencies using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt 
   ```

6. Enter the `src` folder:
   ```bash
   cd src 
   ```

7. Run the pipeline script `composite_transform_pipeline_task2.py`, which will generate the desired output file:
   ```bash
   python3 composite_transform_pipeline_task2.py
   ```

8. To run the unit test for the composite transform, execute the following command:
   ```bash
   python3 test_composite_transform_pipeline_task2.py
   ```
