import argparse


import data_op
import img_op


def argument():
    parser = argparse.ArgumentParser(description="Cellular Automation")
    parser.add_argument("-iter", default=20, type=int)
    parser.add_argument("-rule", default=123, type=int)
    parser.add_argument("-size", default=15, type=int)
    parser.add_argument("-del_img", default=True, type=bool)

    return parser


def main():
    args = argument().parse_args()

    # create basic grid
    grid = data_op.init(iter=args.iter, rule=args.rule)

    # saving first jpg
    img_paths = [f"img/jpg/rule{args.rule}iter1.jpg"]
    img_op.save_jpg(grid, img_paths[0], args.size)

    # run all iteration
    for i in range(args.iter - 1):
        # data operation
        grid = data_op.next_iter(grid)

        # save jpg file
        path = f"img/jpg/rule{args.rule}iter{i+2}.jpg"
        img_paths.append(path)
        img_op.save_jpg(grid, path, args.size)

    # save gif
    img_op.save_gif(img_paths, f"img/gif/rule{args.rule}iter{args.iter}.gif")

    if args.del_img:
        for i in range(1, args.iter):
            img_op.del_jpg(path="img/jpg", file_name=f"rule{args.rule}iter{i}.jpg")


if __name__ == "__main__":
    main()
