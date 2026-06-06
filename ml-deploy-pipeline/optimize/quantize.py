from onnxruntime.quantization import quantize_dynamic, QuantType

print("Quantizing model...")

quantize_dynamic(
    "models/model.onnx",
    "models/model_int8.onnx",
    weight_type=QuantType.QInt8
)

print("Quantized model saved at models/model_int8.onnx")