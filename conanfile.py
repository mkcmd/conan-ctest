from conans import ConanFile, CMake, tools


class CtestConan(ConanFile):
    name = "ctest"
    version = "1.0.0"
    license = "Apache-2.0"
    author = "Bas van den Berg <b.van.den.berg.nl@gmail.com>"
    url = "https://github.com/bvdberg/ctest"
    description = "ctest is a unit test framework for software written in C."
    topics = ("testing")

    def source(self):
        self.run("git clone https://github.com/bvdberg/ctest.git")

    def package(self):
        self.copy("*.h", dst="include", src=".")
