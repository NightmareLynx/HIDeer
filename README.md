![image alt](https://github.com/NightmareLynx/HIDeer/blob/5104779ea053ba851688d4c976587887f472d0e5/Logo.png)
# HIDeer

**Hide messages in plain sight with advanced image steganography**

HIDeer is a powerful steganography tool that allows you to hide and extract secret messages within images using the LSB (Least Significant Bit) technique. Perfect for cybersecurity education, digital forensics learning, and secure communication.

## Features

- **Message Hiding**: Embed text messages invisibly into images
- **Message Extraction**: Retrieve hidden messages from steganographic images
- **Capacity Analysis**: Calculate maximum data storage for any image
- **Robust Error Handling**: Comprehensive validation and user feedback
- **Format Support**: Works with common image formats (JPEG, PNG, BMP)
- **CLI Interface**: Easy-to-use command-line interface

## Quick Start

### Prerequisites

Make sure you have Python 3.6+ installed, then install the required dependency:

```bash
pip install Pillow
```

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/HIDeer.git
cd HIDeer
```

2. Make the script executable (Linux/Mac):

```bash
chmod +x steganography.py
```

## Usage

### Hide a Message

```bash
python steganography.py hide input.jpg "Your secret message" output.png
```

### Extract a Hidden Message

```bash
python steganography.py extract stego_image.png
```

### Analyze Image Capacity

```bash
python steganography.py analyze image.jpg
```

## Command Reference

| Command     | Description                 | Syntax                                            |
| ----------- | --------------------------- | ------------------------------------------------- |
| `hide`    | Hide a message in an image  | `hide <input_image> "<message>" <output_image>` |
| `extract` | Extract hidden message      | `extract <stego_image>`                         |
| `analyze` | Show image storage capacity | `analyze <image>`                               |

## How It Works

HIDeer uses **LSB (Least Significant Bit) steganography**:

1. **Hiding Process**: The tool modifies the least significant bit of each RGB color channel in image pixels
2. **Minimal Visual Impact**: Changes are so small (±1 in color value) they're invisible to human eyes
3. **Data Retrieval**: The extraction process reads these modified bits to reconstruct the hidden message
4. **Message Delimiting**: Uses a special delimiter (`###END###`) to mark message boundaries

### Technical Details

- **Capacity**: 3 bits per pixel (1 per RGB channel)
- **Format**: Saves as PNG to prevent compression artifacts
- **Encoding**: UTF-8 text encoding with binary conversion
- **Security**: Provides data concealment (not encryption)

## Educational Use Cases

Perfect for learning:

- **Digital Forensics**: Understanding data concealment techniques
- **Cybersecurity**: Steganography vs cryptography concepts
- **Binary Operations**: Low-level bit manipulation
- **Image Processing**: Pixel-level data manipulation

## Important Notes

- Use PNG format for output to avoid compression that destroys hidden data
- Original image should have sufficient capacity for your message
- This tool provides **data hiding**, not encryption - combine with encryption for security
- Intended for educational and legitimate security research purposes

## 🛠️ Example Workflow

```bash
# Step 1: Check if your image can hold your message
python steganography.py analyze photo.jpg

# Step 2: Hide your message
python steganography.py hide photo.jpg "This is my secret!" secret_photo.png

# Step 3: Later, extract the message
python steganography.py extract secret_photo.png
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Areas for Contribution

- Additional image formats support
- GUI interface
- Advanced steganography algorithms
- Performance optimizations
- Enhanced security features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Developed for cybersecurity education and research
- Inspired by classical steganography techniques
- Built with Python and Pillow imaging library

---

**⚡ HIDeer - Where secrets hide in plain sight**

*Disclaimer: This tool is intended for educational purposes and legitimate security research. Users are responsible for complying with applicable laws and regulations.*
