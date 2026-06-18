import tiktoken

# Create a tokenizer (encoder) that uses the same tokenization rules as the GPT-4o model.
#
# Different models may use different encodings, so using encoding_for_model() ensures compatibility with the target model.
enc = tiktoken.encoding_for_model("gpt-4o")

# The text we want to convert into tokens.
textToEncode = "Hare Krishna Dear Devotees!"

# Convert the text into a list of token IDs.
#
# A token is a small unit of text. Depending on the text,
# a token may represent:
# - a whole word
# - part of a word
# - punctuation
# - whitespace
tokens = enc.encode(textToEncode)
print("tokens:",tokens)
# OUTPUT : tokens [39, 644, 105025, 63682, 11674, 1962, 268, 0]

# Convert token IDs back into human-readable text.
#
# decode() performs the reverse operation of encode().
decodedOutput = enc.decode([39, 644, 105025, 63682, 11674, 1962, 268, 0])
print("decodedOutput:",decodedOutput)
# OUTPUT : decodedOutput: Hare Krishna Dear Devotees!