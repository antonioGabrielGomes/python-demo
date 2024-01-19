import subprocess

yolo_command = "yolo task=detect mode=train model=yolov8l.pt data=./PlayingCards/data.yaml epochs=50 imgsz=640 | tee /dev/tty"
process = subprocess.Popen(yolo_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

stdout, stderr = process.communicate()

print(stdout.decode('utf-8'))
print(stderr.decode('utf-8'))

exit_code = process.returncode
if exit_code == 0:
    print("\nTreinamento concluído com sucesso!")
else:
    print(f"\nErro durante o treinamento. Código de saída: {exit_code}")
