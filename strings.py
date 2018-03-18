# Input string.
s = "If we took a holiday took some time to celebrate it would be it would be so nice"
n = ""

# Separate on comma.
cities = list(s.split())
i = -1

# Loop and print each city name.
for city in cities:
    n += (cities[i] + " ")
    i -= 1

print(n)