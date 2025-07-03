import random
from datetime import date

# Sample problem set
problems = [
    {
        "topic": "arrays",
        "difficulty": "easy",
        "title": "Two Sum",
        "link": "https://leetcode.com/problems/two-sum/"
    },
    {
        "topic": "trees",
        "difficulty": "medium",
        "title": "Binary Tree Level Order Traversal",
        "link":
        "https://leetcode.com/problems/binary-tree-level-order-traversal/"
    },
    {
        "topic": "dp",
        "difficulty": "hard",
        "title": "Longest Increasing Subsequence",
        "link": "https://leetcode.com/problems/longest-increasing-subsequence/"
    },
    {
        "topic": "linked list",
        "difficulty": "easy",
        "title": "Reverse Linked List",
        "link": "https://leetcode.com/problems/reverse-linked-list/"
    },
    {
        "topic": "graphs",
        "difficulty": "medium",
        "title": "Number of Islands",
        "link": "https://leetcode.com/problems/number-of-islands/"
    },
]

# Simulated memory to avoid repeating topics
memory = [
    {
        "date": "2025-07-01",
        "topic": "arrays"
    },
    {
        "date": "2025-07-02",
        "topic": "linked list"
    },
]


# Get user input
def get_user_input():
    print("\n👋 Welcome to your Daily Coding Interview Practice Agent!")
    level = input("Enter your skill level (beginner/intermediate/advanced): "
                  ).strip().lower()
    topic = input(
        "Enter a topic you want to practice (e.g., arrays, trees, dp): "
    ).strip().lower()
    time = input("How much time do you have (in minutes)? ").strip()
    return level, topic, time


# Filter problems based on topic
def filter_problems(level, topic):
    available = [p for p in problems if p["topic"] == topic]
    if not available:
        print(f"❌ No problems found for topic '{topic}'. Try a different one.")
        return None
    return random.choice(available)


# Check if topic was used recently
def was_topic_recent(topic):
    return any(mem["topic"] == topic for mem in memory[-2:])


# Update memory log
def update_memory(topic):
    today = str(date.today())
    memory.append({"date": today, "topic": topic})
    if len(memory) > 3:
        memory.pop(0)


# Generate and display the challenge
def suggest_challenge(level, topic, time):
    if was_topic_recent(topic):
        print(
            f"\n⚠️ You've recently practiced '{topic}'. Try a different topic for variety."
        )
        return

    suggestion = filter_problems(level, topic)
    if suggestion:
        print("\n✅ **Today's Challenge**")
        print(f"- Topic: {suggestion['topic'].title()}")
        print(f"- Difficulty: {suggestion['difficulty'].title()}")
        print(f"- Problem: {suggestion['title']}")
        print(f"- Link: {suggestion['link']}")
        print("💡 You've got this! 💪")
        update_memory(topic)


# Main program loop
def main():
    level, topic, time = get_user_input()

    # Basic validation
    if not level or not topic:
        print("\n⚠️ Please provide both a skill level and a topic to proceed.")
        return

    suggest_challenge(level, topic, time)


# Run the program
if __name__ == "__main__":
    main()
