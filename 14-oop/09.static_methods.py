# without intialize kisi bhi method ko access karna 


class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    

raw = " water , milk , ginger , honey "

cleaned = ChaiUtils.clean_ingredients(raw) #direct class k method ko accesss karra hai
print(cleaned)


