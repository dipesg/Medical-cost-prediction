from django.shortcuts import render, redirect
import pandas as pd
import pickle

def index_func(request):
    res = 0
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['sex'] # select
        bmi = request.POST['bmi']
        child = request.POST['child']
        smoker = request.POST['smoker'] # select
        region = request.POST['region'] # select

        if name != "":
            df = pd.DataFrame(columns=['age', 'sex', 'bmi', 'children',	'smoker', 'region'])

            df2 = {'age': float(age), 'sex': int(gender), 'bmi': float(bmi), 'children': int(child),
                   'smoker': int(smoker), 'region': int(region)}

            df = df.append(df2, ignore_index=True)
            # load the model from disk
            filename1 = 'polls/Medical.pickle'
            loaded_model = pickle.load(open(filename1, 'rb'))
            res = loaded_model.predict(df)
            print(res)

        else:
            return redirect('homepage')
    else:
        pass

    return render(request, "index.html", {'response': res})
