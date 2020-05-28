from distutils.core import setup, Extension


def main():
    setup(name="sets",
          version="1.0.0",
          description="Python module for generating sets pertinent to discrete math",
          author="Ariel Young",
          author_email="arielyoung103@gmail.com",
          ext_modules=[Extension("sets", ["setsmodule.c"])])


if __name__ == "__main__":
    main()
