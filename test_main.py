import polars as pl
import matplotlib.pyplot as plt
import requests

from main import exploring_data, mean_variable, median_variable, count_variable, hist_plot


def check_exploring_data(path):
    df = pl.read_csv(path)
    if exploring_data(path) is not None:
        return True
    else:
        raise Exception(
            f"Error when checking the existence of the result: {response.status_code}"
            )
    
def check_hist_plot(path, variable):
    df = pl.read_csv(path)
    if hist_plot(path, variable) == "done!":
        return True
    else:
        raise Exception(
            "The histogram has not been generated"
            )


def check_mean_variable(path, variable):
    df = pl.read_csv(path)
    if mean_variable(path, variable) ==  df[variable].mean():
        return True
    else:
        raise Exception(
            f"Error in funtion mean_variable: {response.status_code}"   
        )   
    
def check_median_variable(path, variable):
    df = pl.read_csv(path)
    if median_variable(path, variable) ==  df[variable].median():
        return True
    else:
        raise Exception(
            f"Error in funtion median_variable: {response.status_code}"   
        )      

def check_count_variable(path, variable):
    df = pl.read_csv(path)
    if count_variable(path, variable) == df[variable].sum() / df[variable].mean() :
        return True
    else:
        raise Exception(
            f"Error in funtion count_variable: {response.status_code}"   
        )      
    


def check_github_file_existence(owner, repo, path):
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{path}"

    response = requests.get(url)
    if response.status_code == 200:
        return True
    elif response.status_code == 404:
        return False
    else:
        raise Exception(
            f"Error when checking the existence of the file: {response.status_code}"
        )



if __name__ == "__main__":
    assert check_exploring_data("LinkedInTechJobsDataset.csv")
    assert check_hist_plot("LinkedInTechJobsDataset.csv","Total_applicants")
    assert check_mean_variable("LinkedInTechJobsDataset.csv","Total_applicants")
    assert check_median_variable("LinkedInTechJobsDataset.csv","Total_applicants")
    assert check_count_variable("LinkedInTechJobsDataset.csv","Total_applicants")
    owner = "nogibjj"
    repo = "IDS706_DataEngineering_BarbaraFlores_Miniproject3"
    path1 = "total_applicants.png"
    assert check_github_file_existence(owner, repo, path1)
    path2 = "aggregated_stats.png"
    assert check_github_file_existence(owner, repo, path2)

