#gcex1.py
import gc
print("is GC enabled =",gc.isenabled() )  # True
print("\nThis is a python class")
gc.disable()
print("is GC enabled after disable() =",gc.isenabled() )  # False
print("\nGoing on Destructor Concept:")
gc.enable()
print("is GC enabled after enable() =",gc.isenabled() )  # True
print("\nThis is OOPs")