from src.camera import Camera
from src.geometry import create_vertices
from src.render import draw_wireframe

def main():
    
    center = (0,0,1)
    size = 2

    vertices = create_vertices(center, size)

    print("Cube Verticies")

    for v in vertices:
        print(v)

if __name__ == "__main__":
    main()