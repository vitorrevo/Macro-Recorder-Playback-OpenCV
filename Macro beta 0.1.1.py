import cv2
import sys
import time

def start_recording():
    # Configurar o tamanho do vídeo
    width = 1366
    height = 768
    codec = 'PVG_MJPE'  # Codificador de vídeos
    
    # Iniciar a captura
    video = cv2.VideoCapture(0, codec)
    
    # Variáveis para salvar as gravações
    saving = False
    recorded_data = []
    
    while True:
        if not video.isReading():
            break
            
        frame = video.getFrame()
        
        # Detectar movimentos do mouse
        pos = video.getTrackbarPos('Rodal')
        # Verificar teclas pressionadas
        key = cv2.waitKeyEx(10)
        
        # Salvar os dados se estiver rodando
        if saving:
            window_info = {
                'width': width,
                'height': height,
                'x1': int(frame.x1),
                'y1': int(frame.y1),
                'x2': int(frame.x2),
                'y2': int(frame.y2)
            }
            recorded_data.append(window_info)
            
            # Salvar em arquivo .txt
            with open('macro.txt', 'w') as f:
                for data in recorded_data:
                    f.write(f"{data['x1']} {data['y1']} {data['x2']} {data['y2']}\n")
                    
        # Verificar tecla 'R' para começar a gravar
        if key == ord('R'):
            saving = True
        
        # Verificar tecla 'P' para pausar/continuar
        if key == ord('P'):
            saving = not saving
            
        # Desenhar a janela atual
        cv2.rectangle(frame, (data['x1'], data['y1']), (data['x2'], data['y2']), (0, 255, 0), 2) if saving else None
        video.showWindow()
        
    return recorded_data

def play_back_recorded():
    # Ler os dados salvados
    with open('macro.txt', 'r') as f:
        recorded_data = []
        for line in f:
            x1, y1, x2, y2 = map(int, line.strip().split())
            recorded_data.append({'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2})
    
    # Iniciar a reprodução
    video = cv2.VideoCapture(0)
    replication = []
    
    for data in recorded_data:
        frame = video.getFrame()
        # Replicar as coordenadas
        cv2.rectangle(frame, (data['x1'], data['y1']), (data['x2'], data['y2']), (0, 255, 0), 2)
        replication.append(frame)
        
    # Reproduzir todas as frames
    for frame in replication:
        video.showWindow()
    
def main():
    print("Macro Recorder e Playback - OpenCV")
    print("Press 'R' to start recording\nPress 'P' to pause/continue\nPress 'P' again to stop recording")
    
    # Iniciar ou reproduzir
    action = input().strip() or 'playback'
    
    if action == 'record':
        recorded_data = start_recording()
    elif action == 'playback':
        play_back_recorded()

if __name__ == '__main__':
    main()
