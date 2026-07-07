from flask import Flask,render_template,request,jsonify
import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
api_key=os.getenv("api_key")
client=genai.Client(api_key=api_key)
app=Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/ask',methods=['POST'])
def ask():
    user_input=request.form.get("question")
    response=client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
            )
    answer=(response.text)
    return jsonify({"response": answer})
@app.route('/summarize',methods=['POST'])
def summarize():
    email=request.form.get("email")
    prompt = f"""
                Summarize the following email.

                Include:
                - Main purpose
                - Important points
                - Action items
                - Deadlines (if any)

                Email:
                {email}
                """
    response=client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
            )
    summary=response.text
    return jsonify({"response": summary})
    
if __name__ == "__main__":
    app.run(debug=True)