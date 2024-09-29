import pandas as pd
import random
import os
def generate_sets(file_path, num_sets, num_questions, save_location):
    try:
        questions_df = pd.read_csv(file_path)  
        if 'Question' not in questions_df.columns:
            print("Error: Dataset must have a 'Question' column.")
            return

        total_questions = len(questions_df)

        
        if total_questions < num_questions:
            print(f"Error: Not enough questions in the dataset. You only have {total_questions} questions.")
            return

        
        for set_num in range(1, num_sets + 1):
            set_name = f"Set_{set_num}.txt"
            set_path = os.path.join(save_location, set_name)
            
            
            selected_questions = questions_df['Question'].sample(n=num_questions, replace=False).tolist()

            
            with open(set_path, 'w') as f:
                f.write(f"Question Set {set_num}\n")
                f.write("="*20 + "\n")
                for idx, question in enumerate(selected_questions, 1):
                    f.write(f"{idx}. {question}\n")

            print(f"Set {set_num} saved at {set_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = input("Enter the path to the questions dataset (CSV): ")
num_sets = int(input("Enter the number of sets you want to generate: "))
num_questions = int(input("Enter the number of questions per set: "))
save_location = input("Enter the location where the sets should be saved: ")

generate_sets(file_path, num_sets, num_questions, save_location)
