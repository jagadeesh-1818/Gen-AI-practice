from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

print("Loading model...", flush=True)

llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen2.5-0.5B-Instruct",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 64,
        "do_sample": False,
        "return_full_text": False
    }
)

model = ChatHuggingFace(llm=llm)

print("Model loaded. Type \'exit\' to quit.")

system_message = SystemMessage(content= "Answer questions briefly and directly. For simple questions, give only the answer.")

chat_history = []

while True:
    question = input('\nYou:').strip()

    if question.lower() == 'exit':
        print("Exiting...")
        break

    if not question:
        continue

    chat_history.append(HumanMessage(content= question))
    
    response = model.invoke([system_message] + chat_history)
    
    chat_history.append(AIMessage(content= response.content))

    print(f'\nAI: {response.content}')

print('\nChat History: ')

for message in chat_history:
    print(f'{message.type}: {message.content}')

