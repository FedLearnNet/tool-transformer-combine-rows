from pyfedappwrap.engine.runtime import FedDBEngine

from app import TransformerCombineRows

engine = FedDBEngine()
engine.register_transformer(TransformerCombineRows())

if __name__ == "__main__":
    engine.start()
    engine.wait_until_stop()
