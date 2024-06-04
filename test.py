import imageio 
NUM_AP = 3
count = 37
image_files = [
            "Week8/Output/{}Agent_{}.png".format(NUM_AP, i) for i in range(count + 1)
        ]
images = [imageio.imread(file) for file in image_files]
imageio.mimsave("Week8\Demo\{}_agent.gif".format(NUM_AP), images, fps=7)