# # from backend.extractor import extract_actions

# # transcript = """
# # John: We need to finish the dashboard by Friday.
# # Sarah: I will complete the frontend.
# # Mike: I will prepare the API.
# # """

# # result = extract_actions(transcript)

# # print(result)from backend.extractor import extract_actions

# transcript = """
# John: We need to finish the dashboard by Friday.
# Sarah: I will complete the frontend.
# Mike: I will prepare the API.
# """

# result = extract_actions(transcript)

# print(result)
# print(type(result))
from backend.extractor import extract_actions

transcript = """
John: We need to finish the dashboard by Friday.
Sarah: I will complete the frontend.
Mike: I will prepare the API.
"""

result = extract_actions(transcript)

print(result)
