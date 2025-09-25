import os
import sys
import dill
import pandas as pd
from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        print(f"[save_object] About to save object to {file_path}")
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
        print(f"[save_object] Successfully saved object to {file_path}")

    except Exception as e:
        print(f"[save_object] Exception occurred: {e}")
        raise CustomException(e, sys)