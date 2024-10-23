from openai import OpenAI


client = OpenAI(
    api_key='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'
)


def get_car_ai_bio(model, brand, year):
    message = ''''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.
    Descreva especificações técnicas desse modelo de carro.
    '''
    message = message.format(brand, model, year)
    response = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': message
            }
        ],
        max_tokens=1000,
        model='gpt-3.5-turbo',
    )

    return response.choices[0].message.content