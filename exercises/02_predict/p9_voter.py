def voter_eligibility(name,age):
    if age >= 18:
        return f"{name} - You are eligible to vote."
    else:
        return f"{name} - You are not eligible to vote."
print(voter_eligibility("John", 20))
print(voter_eligibility("Alice", 16))
