
# Background Remover Micro-App

A simple command-line tool for removing backgrounds from images using the `rembg` library in Python. This app allows you to quickly process images with various models and settings for enhanced control over the output.

## Features

- **Background Removal**: Automatically removes backgrounds from images using pre-trained models.
- **Model Selection**: Choose from different models like `u2net`, `u2netp`, `u2net_human_seg`, and `silueta` to optimize for speed or accuracy.
- **Alpha Matting**: Optional support for alpha matting for smoother edge transitions.
- **Threshold Control**: Fine-tune foreground and background thresholds for better transparency control.

## Prerequisites

- **Python 3.8+**: Make sure Python is installed.
- **Virtual Environment**: Recommended for isolated dependency management.
- **Install `rembg`**:
  
  ```bash
  pip install rembg
  ```

  If you're in a managed environment, use a virtual environment:

  ```bash
  python3 -m venv env
  source env/bin/activate  # Use .\env\Scripts\activate on Windows
  pip install rembg
  ```

## Installation

Clone the repository and navigate to the directory:

```bash
git clone https://github.com/dansasser/background-remover-micro-app.git
cd background-remover-micro-app
```

## Usage

### Basic Command

```bash
python remove_bg.py <input_image_path> <output_image_path> <model_name> [alpha_matting] [foreground_threshold] [background_threshold]
```

### Example

Remove the background of an image using the `u2net_human_seg` model with alpha matting:

```bash
python remove_bg.py img/chris01.jpg output/avatar02.png u2net_human_seg 1 250 12
```

- `img/chris01.jpg`: Path to the input image.
- `output/avatar02.png`: Path to save the output image.
- `u2net_human_seg`: Use a model optimized for human segmentation.
- `1`: Enable alpha matting for smoother edges (`1` for True, `0` for False).
- `250`: Foreground threshold for better edge control.
- `12`: Background threshold for improved transparency.

## Models

- **`u2net`**: Default model, balanced for most use cases.
- **`u2netp`**: Smaller and faster, good for quick processing.
- **`u2net_human_seg`**: Optimized for photos where people are the main subject.
- **`silueta`**: Lightweight model for simpler images.

## Troubleshooting

- **Error: `new_session() got multiple values for argument 'model_name'`**  
  Make sure to pass the model via `new_session` in the script. This is handled in the provided `remove_bg.py` script.

- **Unable to install `rembg`**:  
  If you're in a restricted environment, use a virtual environment as shown above.

## Contributing

Feel free to fork this repository and submit pull requests. Suggestions, bug reports, and feature requests are welcome.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

