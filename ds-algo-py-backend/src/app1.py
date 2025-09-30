# import asyncio
# import logging
# import websockets

# from handler import *

# HOST = "localhost"
# PORT = 8765

# if __name__ == "__main__":
#     try:
#         async def main():
#             async with websockets.serve(handler=handler, host=HOST, port=PORT):
#                 logging.info("Server started on ws://%s:%d", HOST, PORT)
#                 await asyncio.Future()
#         asyncio.run(main())
#     except KeyboardInterrupt:
#         logging.info("Server stopped by user.")