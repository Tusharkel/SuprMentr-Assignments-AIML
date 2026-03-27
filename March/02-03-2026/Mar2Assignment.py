'''
*Assignment (02/03/2026)*

*Assignment Name* : ML Idea Generator
*Description* : Suggest ML problems in college, healthcare, shopping and describe input → output.
'''

# ML Idea Generator

ml_ideas = {
    "College": {
        "problem": "Student Performance Prediction",
        "input": ["attendance", "study_hours", "assignment_scores"],
        "output": "predicted_final_grade"
    },

    "Healthcare": {
        "problem": "Disease Risk Prediction",
        "input": ["age", "blood_pressure", "cholesterol", "heart_rate"],
        "output": "disease_risk_probability"
    },

    "Shopping": {
        "problem": "Product Recommendation System",
        "input": ["user_purchase_history", "product_views", "ratings"],
        "output": "recommended_products"
    }
}

for domain, info in ml_ideas.items():
    print("Domain:", domain)
    print("Problem:", info["problem"])
    print("Input:", info["input"])
    print("Output:", info["output"])
    print("-" * 40)