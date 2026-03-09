import atexit
import threading
import queue
import pyttsx3

_engine = pyttsx3.init()
_engine.setProperty("voice", "es")
_engine.setProperty("rate", 150)

_tts_queue = queue.Queue()
_worker_running = True

def _tts_worker():
    while _worker_running:
        try:
            text = _tts_queue.get(timeout=0.5)
            if text:
                _engine.say(text)
                _engine.runAndWait()
            _tts_queue.task_done()
        except queue.Empty:
            continue
        except Exception as e:
            print(f"TTS error: {e}")

_worker_thread = threading.Thread(target=_tts_worker, daemon=True)
_worker_thread.start()

@atexit.register
def _shutdown_tts():
    global _worker_running
    _worker_running = False
    try:
        _engine.stop()
    except Exception:
        pass

def text_voice(text: str):
    """No bloquea: encola el texto y retorna inmediatamente"""
    _tts_queue.put(text)

