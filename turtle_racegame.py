import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("🐢 Turtle Race Game!")
screen.bgcolor("white")
screen.setup(width=800, height=600)

# Race settings
COLORS = ["red", "blue", "orange", "purple", "pink", "black"]
NAMES  = ["Red", "Blue", "Orange", "Purple", "Pink", "Black"]
NUM_TURTLES = 6
FINISH_LINE = 340
START_X = -340
LANE_SPACING = 80
FIRST_LANE_Y = 200

# Draw track
def draw_track():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.penup()

    # Finish line
    pen.goto(FINISH_LINE, 260)
    pen.pendown()
    pen.pensize(4)
    pen.color("black")
    pen.goto(FINISH_LINE, -220)
    pen.penup()

    # Finish label
    pen.goto(FINISH_LINE + 10, 230)
    pen.color("black")
    pen.write("FINISH", font=("Arial", 14, "bold"))

    # Start line
    pen.goto(START_X, 260)
    pen.pendown()
    pen.pensize(2)
    pen.color("gray")
    pen.goto(START_X, -220)
    pen.penup()

    # Lane lines
    pen.pensize(1)
    pen.color("black")
    for i in range(NUM_TURTLES + 1):
        y = FIRST_LANE_Y + 40 - i * LANE_SPACING
        pen.goto(START_X, y)
        pen.pendown()
        pen.goto(FINISH_LINE, y)
        pen.penup()

    # Title
    pen.goto(0, 260)
    pen.color("black")
    pen.write("🐢 TURTLE RACE 🐢", align="center", font=("Arial", 22, "bold"))

draw_track()

# Create turtles
racers = []
for i in range(NUM_TURTLES):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(COLORS[i])
    t.penup()
    t.speed(0)
    y = FIRST_LANE_Y - i * LANE_SPACING
    t.goto(START_X, y)
    t.setheading(0)  # makes them face right
    racers.append(t)

# Labels on the left
label_pen = turtle.Turtle()
label_pen.hideturtle()
label_pen.penup()
label_pen.speed(0)
for i in range(NUM_TURTLES):
    y = FIRST_LANE_Y - i * LANE_SPACING - 8
    label_pen.goto(START_X - 50, y)
    label_pen.color(COLORS[i])
    label_pen.write(NAMES[i], align="right", font=("Arial", 11, "bold"))

# Status display turtle
status = turtle.Turtle()
status.hideturtle()
status.penup()
status.speed(0)

def show_status(msg, color="white"):
    status.clear()
    status.goto(0, -270)
    status.color(color)
    status.write(msg, align="center", font=("Arial", 15, "bold"))

# Ask for bet
show_status("Click anywhere to start the race!", "white")

bet = screen.textinput(
    "Give Your Bet Turtle!",
    f"Which turtle will win?\nChoose: {', '.join(NAMES)}"
)

if bet:
    bet = bet.strip().capitalize()
    if bet in NAMES:
        show_status(f"You bet on {bet}! Click to start!", "black")
    else:
        bet = None
        show_status("Invalid bet. Watching for fun! Click to start.", "gray")
else:
    show_status("No bet placed. Click to start!", "gray")

# Wait for click to start
#if False else None  # placeholder
clicked = []
def on_click(x, y):
    if not clicked:
        clicked.append(True)
screen.onscreenclick(on_click)

# Wait until clicked
while not clicked:
    screen.update()

screen.onscreenclick(None)
show_status("🏁 RACE IN PROGRESS...", "red")

# Race loop
winner = None
while winner is None:
    for i, t in enumerate(racers):
        dist = random.randint(1, 10)
        t.forward(dist)
        if t.xcor() >= FINISH_LINE:
            winner = NAMES[i]
            winner_color = COLORS[i]
            break
    screen.update()

# Show result
if bet and bet == winner:
    msg = f"🏆 {winner} WINS!  ✅ You guessed right! CONGRATULATIONS!"
    msg_color = "darkgreen"
elif bet:
    msg = f"🏆 {winner} WINS!  ❌ {bet} lost. Better luck next time!"
    msg_color = "red"
else:
    msg = f"🏆 {winner} WINS! 🎉"
    msg_color = "darkgreen"

show_status(msg, msg_color)

# Highlight winner
for i, t in enumerate(racers):
    if NAMES[i] == winner:
        t.shapesize(2, 2)

print(f"\n winner: {winner}")
turtle.done()
