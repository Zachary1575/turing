CXX := clang++ # For MacOS. Want to use the llvm version.
CXXFLAGS := -fcolor-diagnostics -fansi-escape-codes -std=c++17 -g

SRC := ./main.cpp
OBJ := $(SRC:.cpp=.o)
TARGET := main

$(TARGET): $(OBJ) # Object Files ---> Binary
	$(CXX) $(CXXFLAGS) -o $@ $^

%.o: %.cpp # cpp Files --> Object Files
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) $(TARGET)

# Phony Targets
.PHONY: all clean
