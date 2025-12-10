import json
import os


# Physics Objective 

# classification_filename = {
#     "Fields\Mathematical_Reasoning.json": [
#         0, 1, 2, 4, 7, 8, 9, 12, 15, 16, 17, 18, 20, 21, 23, 24,
#         28, 29, 32, 33, 34, 36, 37, 39, 40, 41, 42, 44, 45, 47,
#         49, 50, 51, 53, 54, 56, 57, 59, 60, 62, 63, 65, 66, 68,
#         69, 71, 72, 74, 75, 77, 78, 80
#     ],
#     "Fields\Logical_Reasoning.json": [
#         0, 2, 3, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 19, 22, 25,
#         26, 27, 30, 31, 35, 38, 43, 46, 48, 50, 52, 55, 58, 61,
#         64, 67, 70, 73, 76, 79
#     ],
#     "Fields\Lang_Comp_and_Produc.json": [],
#     "Fields\Natural_Science.json": [],
#     "Fields\Sociocultural_Understanding.json": [],
#     "Fields\Data_and_StatisticalLiteracy.json": [],
#     "Fields\Commonsense_and_WorldKnowledge.json": [
#         1, 5, 6, 7, 10, 13, 21, 31, 52, 67, 70
#     ],
#     "Fields\Creative_and_Open-ended_Questions.json": [],
# }

# Chemistry Objective 

classification_filename = {
    "Fields/Mathematical_Reasoning.json": [
        1, 4, 6, 7, 14, 15, 16, 25, 26, 35, 36, 44, 45, 47, 60, 67, 74, 79, 82, 92, 98, 107, 121, 126
    ],
    "Fields/Logical_Reasoning.json": [
        0, 2, 3, 5, 8, 9, 10, 11, 12, 13, 18, 20, 21, 22, 23, 24, 27, 28, 29, 30, 31, 32, 33, 34, 37, 38, 39, 40, 41, 42, 43, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 61, 62, 64, 65, 66, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 80, 81, 83, 84, 85, 86, 87, 88, 89, 90, 91, 93, 94, 95, 96, 97, 99, 100, 101, 102, 103, 104, 105, 106, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142
    ],
    "Fields/Lang_Comp_and_Produc.json": [
    ],
    "Fields/Natural_Science.json": [
    ],
    "Fields/Sociocultural_Understanding.json": [
    ],
    "Fields/Data_and_StatisticalLiteracy.json": [
        17, 39, 73, 84, 123
    ],
    "Fields/Commonsense_and_WorldKnowledge.json": [
        1, 12, 13, 19, 28, 32, 37, 41, 46, 50, 57, 62, 63, 66, 71, 76, 77, 85, 89, 91, 95, 100, 104, 106, 110, 113, 116, 119, 124, 131, 133, 136, 139
    ],
    "Fields/Creative_and_Open-ended_Questions.json": []
}

# Biology Objective

# classification_filename = {
#     "Fields/Mathematical_Reasoning.json": [
#         17, 41, 52, 57, 63, 71, 105, 111, 113, 138, 149, 154, 159, 164],
#     "Fields/Logical_Reasoning.json": [
#         4, 8, 13, 28, 38, 40, 42, 58, 63, 67, 70, 77, 90, 91, 92, 94, 96, 99, 102, 104, 109, 116, 117, 120, 121, 123, 125, 127, 128, 129, 132, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179],
#     "Fields/Lang_Comp_and_Produc.json": [],
#     "Fields/Natural_Science.json": [],
#     "Fields/Sociocultural_Understanding.json": [
#         ],
#     "Fields/Data_and_StatisticalLiteracy.json": [
#         17, 41, 57, 76, 94, 105, 111, 113, 117, 138, 149, 154, 159, 163, 164],
#     "Fields/Commonsense_and_WorldKnowledge.json": [
#         5, 7, 25, 27, 32, 37, 51, 54, 59, 61, 62, 65, 69, 75, 80, 86, 87, 90, 91, 93, 95, 97, 98, 103, 104, 106, 107, 108, 110, 112, 114, 115, 118, 119, 122, 125, 126, 128, 130, 131, 134, 135, 136, 140, 141, 145, 146, 147, 148, 151, 152, 153, 154, 155, 156, 157, 158, 160, 161, 162, 165, 166, 167, 168, 170, 171, 173, 176, 177, 178, 179],
#     "Fields/Creative_and_Open-ended_Questions.json": []
# }

# Political_Science Objective
# classification_filename = {
#     "Fields/Mathematical_Reasoning.json": [
#     ],
#     "Fields/Logical_Reasoning.json": [
#         0, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 20, 21, 22, 23, 31, 32, 33, 34, 35, 43, 44, 45, 46, 47, 56, 57, 58, 59, 66, 69, 70, 71, 81, 82, 83, 90, 93, 94, 95, 103, 106, 107, 110, 112, 113, 116, 117, 118, 119, 128, 129, 130, 131, 139, 140, 141, 142, 151, 152, 153, 154, 164, 165, 166, 176, 177, 178, 189, 190, 200, 201, 202, 211, 212, 221, 222, 232, 233, 243, 244, 254, 255, 264, 265
#     ],
#     "Fields/Lang_Comp_and_Produc.json": [
#         31, 79, 92, 104, 127, 138, 174, 208, 219, 252, 263
#     ],
#     "Fields/Natural_Science.json": [
#     ],
#     "Fields/Sociocultural_Understanding.json": [
#     ],
#     "Fields/Data_and_StatisticalLiteracy.json": [
#         36, 44, 61, 67, 74, 79, 82, 121, 156, 157, 182, 193, 224, 247, 248
#     ],
#     "Fields/Commonsense_and_WorldKnowledge.json": [
#         13, 14, 28, 32, 36, 39, 41, 61, 63, 70, 76, 77, 86, 87, 98, 99, 100, 102, 133, 146, 147, 148, 170, 171, 172, 195, 196, 198, 199, 203, 204, 205, 207, 213, 217, 218, 235, 237, 241, 245, 253, 256, 260, 262
#     ],
#     "Fields/Creative_and_Open-ended_Questions.json": [
#         11, 19, 38, 47, 69, 83, 108, 115, 127, 129, 152, 153, 163, 221, 232, 244, 253
#     ]
# }

# History Objective

# classification_filename = {
#     "Fields/Mathematical_Reasoning.json": [
#     ],
#     "Fields/Logical_Reasoning.json": [
#         2, 5, 11, 12, 23, 33, 34, 49, 53, 61, 84, 97, 103, 112, 127, 133, 142, 148, 152, 153, 161, 169, 183, 190, 211, 230, 232, 263, 272, 275, 284, 305, 312, 316, 334, 335, 342
#     ],
#     "Fields/Lang_Comp_and_Produc.json": [
#         21, 33, 42, 43, 84, 88, 89, 118, 148, 156, 183, 213, 246, 247, 276, 287, 298, 332
#     ],
#     "Fields/Natural_Science.json": [
#     ],
#     "Fields/Sociocultural_Understanding.json": [
#         0, 1, 4, 6, 7, 8, 9, 10, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 35, 37, 38, 39, 40, 41, 44, 45, 46, 47, 50, 51, 52, 54, 55, 56, 57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 79, 80, 81, 82, 83, 85, 86, 87, 90, 91, 94, 95, 96, 98, 99, 100, 101, 105, 106, 107, 108, 109, 110, 111, 114, 115, 116, 117, 119, 120, 121, 123, 124, 125, 126, 128, 129, 130, 131, 132, 135, 136, 137, 138, 139, 140, 141, 143, 144, 145, 146, 149, 150, 151, 154, 155, 157, 158, 159, 160, 162, 163, 164, 165, 166, 167, 168, 170, 171, 172, 173, 174, 175, 176, 177, 179, 180, 181, 184, 185, 186, 187, 188, 189, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 203, 204, 205, 206, 207, 208, 209, 210, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 224, 225, 226, 227, 228, 229, 231, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 255, 256, 257, 258, 259, 260, 261, 262, 264, 265, 267, 268, 269, 270, 271, 273, 274, 276, 277, 278, 279, 280, 281, 282, 283, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 299, 300, 301, 302, 303, 304, 306, 307, 308, 309, 310, 311, 313, 314, 315, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 333, 336, 337, 338, 339, 340, 341, 343, 344, 345, 346, 347, 348, 349, 350, 351
#     ],
#     "Fields/Data_and_StatisticalLiteracy.json": [
#         3, 78, 93, 104, 113, 134, 147, 178, 182, 202, 223, 247, 266, 326
#     ],
#     "Fields/Commonsense_and_WorldKnowledge.json": [
#         4, 13, 25, 39, 46, 53, 61, 76, 77, 91, 93, 113, 161, 195, 196, 203, 204, 211, 213, 253, 287, 298, 317, 331, 351
#     ],
#     "Fields/Creative_and_Open-ended_Questions.json": [
#     ]
# }

# Geography Objective



# source_file = "ObjectiveProblems/2010-2025_Physics_MCQs.json"   # 题目源文件
source_file = "ObjectiveProblems/2010-2025_Chemistry_MCQs.json"  
# source_file = "ObjectiveProblems/2010-2025_Biology_MCQs.json"  
# source_file = "ObjectiveProblems/2010-2025_Political_Science_MCQs.json"  
# source_file = "ObjectiveProblems/2010-2025_History_MCQs.json"  
# source_file = "ObjectiveProblems/2010-2025_Geography_MCQs.json"  
# -------------------------------
# 1. 读取源 JSON（含 questions 数组）
# -------------------------------
with open(source_file, "r", encoding="utf-8") as f:
    source_data = json.load(f)

source_questions = source_data["questions"]

# 建一个 index → question 映射表
index_map = {q["index"]: q for q in source_questions}

# -------------------------------
# 2. 处理每个分类文件
# -------------------------------
for filename, idx_list in classification_filename.items():

    # # ---- 若目标文件不存在 → 创建空模板 ----
    # if not os.path.exists(filename):
    #     os.makedirs(os.path.dirname(filename), exist_ok=True)
    #     empty_content = {"keywords": "", "questions": []}
    #     with open(filename, "w", encoding="utf-8") as f:
    #         json.dump(empty_content, f, ensure_ascii=False, indent=4)

    # ---- 读取已有文件 ----
    with open(filename, "r", encoding="utf-8") as f:
        target_data = json.load(f)

    # 若不存在 questions 字段，补一个
    if "questions" not in target_data:
        target_data["questions"] = []

    # ---- 根据 index 追加内容 ----
    for idx in idx_list:
        if idx in index_map:
            target_data["questions"].append(index_map[idx])
        else:
            print(f"[警告] 源文件中找不到 index={idx}")

    # ---- 写回文件（不覆盖已有 questions，只是追加） ----
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(target_data, f, ensure_ascii=False, indent=4)

    print(f"已写入：{filename} 追加 {len(idx_list)} 个题目")


