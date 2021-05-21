"""FastApi implementation."""
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
def start_page() -> None:
    """Start page."""
    return FileResponse("./templates/startpage_fast.html")


@app.get("/heatmap")
def heatmap() -> None:
    """Heatmap page."""
    return FileResponse("./templates/heatmap.html")


@app.get("/histograms")
def hist_main() -> None:
    """Histograms main page."""
    return FileResponse("./templates/histograms.html")


@app.get("/Санкт-Петербург")
def hist_spb() -> None:
    """Spb histogram."""
    return FileResponse("./static/Санкт-Петербург.png")


@app.get("/Москва")
def hist_msc() -> None:
    """Moscow histogram."""
    return FileResponse("./static/Москва.png")


@app.get("/Екатеринбург")
def hist_ekb() -> None:
    """Ekb histogram."""
    return FileResponse("./static/Екатеринбург.png")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
