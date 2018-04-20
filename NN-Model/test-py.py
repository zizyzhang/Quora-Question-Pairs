df = pd.DataFrame({"id":['0',"1"],"qid1":['1','3'],"qid2":['2','4'],"question1":["What is the step by step guide to invest in share market in india?","What is the step by step guide to invest in share market in india?"],"question2":["What is the step by step guide to invest in share market?","What would happen if the Indian government stole the Kohinoor (Koh-i-Noor) diamond back?"],"is_duplicate":['0','0']})

"0","1","2","What is the step by step guide to invest in share market in india?","What is the step by step guide to invest in share market?","0"
"1","3","4","What is the story of Kohinoor (Koh-i-Noor) Diamond?","What would happen if the Indian government stole the Kohinoor (Koh-i-Noor) diamond back?","0"
"2","5","6","How can I increase the speed of my internet connection while using a VPN?","How can Internet speed be increased by hacking through DNS?","0"
"3","7","8","Why am I mentally very lonely? How can I solve it?","Find the remainder when [math]23^{24}[/math] is divided by 24,23?","0"
"4","9","10","Which one dissolve in water quikly sugar, salt, methane and carbon di oxide?","Which fish would survive in salt water?","0"

df = pd.read_csv('server-test.csv')
df["question1"] = df["question1"].fillna("").apply(preprocess)
df["question2"] = df["question2"].fillna("").apply(preprocess)
q1s_test, q2s_test, test_q_features = extract_features(df)
test_data_1 = pad_sequences(tokenizer.texts_to_sequences(q1s_test), maxlen=MAX_SEQUENCE_LENGTH)
test_data_2 = pad_sequences(tokenizer.texts_to_sequences(q2s_test), maxlen=MAX_SEQUENCE_LENGTH)
preds = model.predict([test_data_1, test_data_2, features_test], batch_size=BATCH_SIZE, verbose=1);
fpreds = [round(i[0]) for i in preds]
fpreds[0:100]


df = pd.read_csv('server-test2.csv')
df["question1"] = df["question1"].fillna("").apply(preprocess)
df["question2"] = df["question2"].fillna("").apply(preprocess)
q1s_test, q2s_test, test_q_features = extract_features(df)
test_data_1 = pad_sequences(tokenizer.texts_to_sequences(q1s_test), maxlen=MAX_SEQUENCE_LENGTH)
test_data_2 = pad_sequences(tokenizer.texts_to_sequences(q2s_test), maxlen=MAX_SEQUENCE_LENGTH)
preds = model.predict([test_data_1, test_data_2, features_test], batch_size=BATCH_SIZE, verbose=1);
fpreds2 = [round(i[0]) for i in preds]
fpreds2[0:100]==fpreds[0:100]

[0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

[0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

