import tiktoken

# step 1 : get an encoder
enc = tiktoken.encoding_for_model("gpt-4o") # we want to create an encoder for gpt-4o model

textToEncode = "Hare Krishna Dear Devotees!" # the text that we want to encode

tokens = enc.encode(textToEncode) # encode the text
print("tokens:",tokens) # logs the tokens
# OUTPUT : tokens [39, 644, 105025, 63682, 11674, 1962, 268, 0]

decodedOutput = enc.decode([39, 644, 105025, 63682, 11674, 1962, 268, 0]) # decode the encoded text
print("decodedOutput:",decodedOutput) # logs the decodedOutput
# OUTPUT : decodedOutput: Hare Krishna Dear Devotees!