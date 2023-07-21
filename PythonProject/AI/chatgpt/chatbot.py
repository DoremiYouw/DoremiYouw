import openai

class chatgpt():
    def __init__(self,model="gpt-3.5-turbo",max_token=256):
        self.message = []
        self.model = model
        self.max_token = max_token

    def ask_a_question(self):
        print("User:",end="")
        que = input()
        a_message = {"role":"user", "content":que}
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[a_message],
            temperature=1
        )
        answer = completion.choices[0]["message"]["content"]
        print("Bot:",answer)

    def conversation(self):
        self.message = []
        print("Describe the role of the bot:", end="")
        system_def = input()
        self.message.append({"role": "system","content":system_def})
        while True:
            print("User:", end="")
            que = input()
            if que=="quit":
                break
            a_message = {"role":"user", "content":que}
            self.message.append(a_message)
            completion = openai.ChatCompletion.create(
                model=self.model,
                messages=self.message,
                temperature=1
            )
            answer = completion.choices[0]["message"]["content"]
            print("Bot:",answer)
            bot_message = {"role":"assistant", "content":answer}
            self.message.append(bot_message)

            token = 0
            for message in self.message:
                token = token + int(len(message["content"])/3)
            if token>self.max_token:
                print("当前对话长度已达最大值，将只保留最后一次提问的信息。")
                self.message = []
                self.message.append({"role": "system", "content": system_def})
                self.message.append(a_message)
                self.message.append(bot_message)


    def draw_a_picture(self):
        return 0

if __name__ == '__main__':
    openai.api_key = "" #自己的API key
    bot = chatgpt()
    function = 1
    if function==1 :
        bot.ask_a_question()
    else:
        bot.conversation()