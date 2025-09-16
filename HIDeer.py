#!/usr/bin/env python3
"""
Image Steganography Tool
A tool to hide and extract secret messages in images using LSB (Least Significant Bit) technique.
Perfect for cybersecurity learning and data concealment practice.
"""

from PIL import Image
import argparse
import sys
import os

class SteganographyTool:
    def __init__(self):
        self.delimiter = "###END###"  # Marks the end of hidden message
    
    def text_to_binary(self, text):
        """Convert text to binary representation"""
        return ''.join(format(ord(char), '08b') for char in text)
    
    def binary_to_text(self, binary):
        """Convert binary to text"""
        text = ''
        for i in range(0, len(binary), 8):
            byte = binary[i:i+8]
            if len(byte) == 8:
                text += chr(int(byte, 2))
        return text
    
    def hide_message(self, image_path, message, output_path):
        """Hide a message in an image using LSB steganography"""
        try:
            # Open the image
            img = Image.open(image_path)
            img = img.convert('RGB')  # Ensure RGB format
            
            # Add delimiter to mark end of message
            message_with_delimiter = message + self.delimiter
            binary_message = self.text_to_binary(message_with_delimiter)
            
            # Get image dimensions
            width, height = img.size
            max_capacity = width * height * 3  # 3 channels (RGB)
            
            # Check if image can hold the message
            if len(binary_message) > max_capacity:
                raise ValueError(f"Message too long! Image can hold max {max_capacity} bits, "
                               f"but message needs {len(binary_message)} bits")
            
            # Convert image to list of pixels
            pixels = list(img.getdata())
            
            # Hide message in LSBs
            message_index = 0
            modified_pixels = []
            
            for pixel in pixels:
                r, g, b = pixel
                
                # Modify LSB of each color channel if we still have message bits
                if message_index < len(binary_message):
                    # Modify red channel LSB
                    r = (r & 0xFE) | int(binary_message[message_index])
                    message_index += 1
                
                if message_index < len(binary_message):
                    # Modify green channel LSB
                    g = (g & 0xFE) | int(binary_message[message_index])
                    message_index += 1
                
                if message_index < len(binary_message):
                    # Modify blue channel LSB
                    b = (b & 0xFE) | int(binary_message[message_index])
                    message_index += 1
                
                modified_pixels.append((r, g, b))
                
                # Break if we've embedded the entire message
                if message_index >= len(binary_message):
                    # Add remaining unmodified pixels
                    modified_pixels.extend(pixels[len(modified_pixels):])
                    break
            
            # Create new image with modified pixels
            stego_img = Image.new('RGB', (width, height))
            stego_img.putdata(modified_pixels)
            
            # Save the image
            stego_img.save(output_path, 'PNG')  # Use PNG to avoid compression artifacts
            
            print(f"✓ Message successfully hidden in {output_path}")
            print(f"  Original image: {image_path}")
            print(f"  Message length: {len(message)} characters")
            print(f"  Binary bits used: {len(binary_message)}")
            
        except Exception as e:
            print(f"✗ Error hiding message: {str(e)}")
            return False
        
        return True
    
    def extract_message(self, image_path):
        """Extract hidden message from an image"""
        try:
            # Open the image
            img = Image.open(image_path)
            img = img.convert('RGB')
            
            # Get all pixels
            pixels = list(img.getdata())
            
            # Extract LSBs
            binary_message = ''
            
            for pixel in pixels:
                r, g, b = pixel
                
                # Extract LSB from each channel
                binary_message += str(r & 1)  # Red channel LSB
                binary_message += str(g & 1)  # Green channel LSB
                binary_message += str(b & 1)  # Blue channel LSB
            
            # Convert binary to text
            extracted_text = self.binary_to_text(binary_message)
            
            # Find the delimiter to get the actual message
            if self.delimiter in extracted_text:
                message = extracted_text.split(self.delimiter)[0]
                print(f"✓ Message extracted successfully:")
                print(f"  Hidden message: '{message}'")
                print(f"  Message length: {len(message)} characters")
                return message
            else:
                print("✗ No hidden message found or image may be corrupted")
                return None
                
        except Exception as e:
            print(f"✗ Error extracting message: {str(e)}")
            return None
    
    def analyze_image_capacity(self, image_path):
        """Analyze how much data an image can hold"""
        try:
            img = Image.open(image_path)
            width, height = img.size
            
            # Calculate capacity (3 bits per pixel for RGB)
            max_bits = width * height * 3
            max_chars = max_bits // 8  # 8 bits per character
            
            print(f"Image Capacity Analysis:")
            print(f"  Image: {image_path}")
            print(f"  Dimensions: {width}x{height}")
            print(f"  Maximum bits: {max_bits}")
            print(f"  Maximum characters: {max_chars}")
            print(f"  Maximum message length: ~{max_chars - len(self.delimiter)} characters")
            
            return max_chars
            
        except Exception as e:
            print(f"✗ Error analyzing image: {str(e)}")
            return 0

def main():
    tool = SteganographyTool()
    
    parser = argparse.ArgumentParser(
        description="Image Steganography Tool - Hide and extract messages in images",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Hide a message in an image
  python steganography.py hide input.jpg "Secret message" output.png
  
  # Extract a hidden message
  python steganography.py extract stego_image.png
  
  # Check image capacity
  python steganography.py analyze input.jpg
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Hide command
    hide_parser = subparsers.add_parser('hide', help='Hide a message in an image')
    hide_parser.add_argument('input_image', help='Input image file')
    hide_parser.add_argument('message', help='Message to hide')
    hide_parser.add_argument('output_image', help='Output image file (recommended: .png)')
    
    # Extract command
    extract_parser = subparsers.add_parser('extract', help='Extract message from an image')
    extract_parser.add_argument('input_image', help='Image with hidden message')
    
    # Analyze command
    analyze_parser = subparsers.add_parser('analyze', help='Analyze image capacity')
    analyze_parser.add_argument('input_image', help='Image to analyze')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Validate input files exist
    if hasattr(args, 'input_image') and not os.path.exists(args.input_image):
        print(f"✗ Error: Input file '{args.input_image}' not found")
        return
    
    # Execute commands
    if args.command == 'hide':
        tool.hide_message(args.input_image, args.message, args.output_image)
        
    elif args.command == 'extract':
        tool.extract_message(args.input_image)
        
    elif args.command == 'analyze':
        tool.analyze_image_capacity(args.input_image)

if __name__ == "__main__":
    print("🔐 Image Steganography Tool")
    print("=" * 40)
    main()