import streamlit as sl
import pandas as pd
import joblib

path = r"D:\other\Epsilon\Epsilon Training\project 2\my solution_project_2\save files"

column = joblib.load(f"{path}\\input.h5")
model = joblib.load(f"{path}\\model.h5")
Loan_Amount_Term = joblib.load(f"{path}\\Loan_Amount_Term.h5")


    
def Change(param, value):
    return print(f"{param} is change to :  {value}")


def pred(gender, married, dependents, education, employed, income, coap_income, load, term, hist, area):
    test_df = pd.DataFrame(columns = column)
    test_df.at[0,"Gender"] = gender
    test_df.at[0,"Married"] = married
    test_df.at[0,"Dependents"] = dependents
    test_df.at[0,"Education"] = education
    test_df.at[0,"Self_Employed"] = employed
    test_df.at[0,"ApplicantIncome"] = income
    test_df.at[0,"CoapplicantIncome"] = coap_income
    test_df.at[0,"LoanAmount"] = load
    test_df.at[0,"Loan_Amount_Term"] = term
    test_df.at[0,"Credit_History"] = hist
    test_df.at[0,"Property_Area"] = area
    result = model.predict(test_df)[0]
    return result, test_df


sl.markdown("""

<style>

    .css-9s5bis.edgvbvh3{
        display:none;
    }
    
    .css-1q1n0ol.egzxvld0
    {
        display: none;    
    }

<style>
            """, unsafe_allow_html=True)



sl.markdown("<h1>Loan Project</h1", unsafe_allow_html=True)


#-----------------------------------------------------------------------------
with sl.form("Form", clear_on_submit=True):
    #-------------------------------frist row-------------------------------
    col1, col2 = sl.columns(2)
    
    gender = col1.radio("Please inter your Gender", options=("Male", "Female"))
    Change("Gender", gender)
    
    married = col2.radio("Do you Married ?", options=("Yes", "No"))
    Change("married", married)
    
    # -----------------------------------------------------
    
    dependents = sl.selectbox("number of Dependencies", options=([0, 1, 2, "+3"]))
    Change("Dependents number ", dependents)
    if dependents == "+3":
        dependents = 1
        
    else:
        pass

    education = sl.selectbox("inter your Education status", options=(['Graduate', 'Not Graduate']))
    Change("Education status", education)
    
    employed = sl.selectbox("are you Self Employed ?", options=tuple(("Yes", "No")))
    Change("Self Employed", employed)
    
    
    income = sl.slider("please select your Income in month: ", min_value=150, max_value=81000, value=200)
    Change("ApplicantIncome", income)

    coap_income = sl.slider("what is the Coapplicant Income in month ?", min_value=0, max_value=5701, value=200)
    Change("Coapplicant Income", coap_income)
    
    
    load = sl.slider("What is the LoanAmount that you wont ?", min_value=9000, max_value=650000, value=500)
    Change("LoanAmount", load)
    load = load / 1000
    
    term = sl.selectbox("Number of months to repay the loan", options=(Loan_Amount_Term))
    Change("Loan Amount_Term", term)
    
    
    hist = sl.selectbox("what is her Credit History ?", options=(["Good", "Not Good"]))
    sl.write("History of repay the loan")
    Change("Credit_History", hist)
    if hist == "Good":
        hist = 1
    
    else:
        hist = 0
    
    area = sl.selectbox("inter The location of the property", options=(['Urban', 'Rural', 'Semiurban']))
    Change("Property_Area", area)
    
    
    input_data = [gender, married, dependents, education, employed, 
                  income, coap_income, load, term, hist, area]
    
    print(f"all input values : {input_data}")
    
    predict = sl.form_submit_button("predict")
    
    
    if predict:           

        try: 
            result = pred(gender, married, dependents, education, employed, income, coap_income, load, term, hist, area)
            prediction = result[0]
            data = result[-1]
        except:
            sl.warning("Sorry Error in Model procse !")
            print("Sorry Error in Model procse !")
            
        if prediction == 1:
            message = "congratulation Your application for a loan has been accepted"
                        
        else:
            message = "Sorry Your application for a loan has been not accepted"
                        

        print(message)
        sl.subheader("Your Data")
        sl.table(data.transpose())
        # -------------------------------------------------------------
        sl.write(message)
        sl.success("submitted successful")
        print("\n", "-"*100, "\n")