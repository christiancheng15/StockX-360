# StockX 360° GIF Generator

### Generate 360° GIF images from StockX and showcase product from all angles. Enhance online presentations and engage your audience with dynamic visual content. This project was initially created as a concept to generate dynamic Instagram posts. The aim was to allow customers to easily view product designs from all angles, addressing one of the biggest requests. 

## Features
- 360° GIFs: Automatically convert images into smooth, looping GIFs that showcase products from all angles.
- Easy-to-Use: Simple command-line interface for generating GIFs with minimal setup.
- Customizable Rotation Direction: Choose betweeb clockwise and counterclockwise rotation when generating GIFs.

## Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.x
- requests
- bs4
- imageio

## Installation
1. Clone the repository
```bash
git clone https://github.com/christiancheng15/StockX-360.git
cd StockX-360
```

2. Install the necessary Python libraries:
```bash
pip install -r requirements.txt
```

## Usage
To generate 360° GIFs:
1. Run the script with the desired URL from StockX:
```bash
python main.py --url <STOCKX_URL> --clockwise 1
```
Replace <STOCKX_URL> with the desired URL from StockX. Use `--clockwise 1` for a clockwise rotation or `--clockwise 0` for a counterclockwise rotation.

2. The script will scrape the necessary images and generate a GIF, saving it to the `output` directory.

## Output
The generated GIFs will be saved in the output folder within the project directory. Each GIF will be named according to the URL path for easy identification. e.g. air-jordan-1-retro-high-og-chicago-reimagined-lost-and-found.gif

## Example
```bash
python main.py --url https://stockx.com/air-jordan-1-retro-high-og-chicago-reimagined-lost-and-found --clockwise 1
```
This will generate a 360° GIF of the Air Jordan 1 Retro High OG Chicago Reimagined Lost and Found with a clockwise rotation as shown below:
![Air Jordan 1 Retro High OG Chicago Reimagined Lost and Found GIF](examples/air-jordan-1-retro-high-og-chicago-reimagined-lost-and-found.gif)

## Troubleshooting
- Scraping Issues: If the script fails to scrape images, ensure that the URL is correct and that StockX's website structure has not changed.
- Missing Dependencies: Make sure all required Python libraries are installed. You can install them with `pip install -r requirements.txt`.

## Contributing
Contributions are welcome! If you have ideas for new features or improvements, feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

## Contact
For any questions or inquires, please contact [christiancheng15](https://github.com/christiancheng15/).
