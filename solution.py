def file_processor():
    """
    A program that reads a file, modifies its content, and writes to a new file
    with comprehensive error handling.
    """
    
    print("📁 File Processor - Read, Modify, and Write Files")
    print("=" * 50)
    
    # Get input filename with error handling
    while True:
        try:
            input_filename = input("Enter the input filename: ").strip()
            
            if not input_filename:
                print("❌ Error: Filename cannot be empty. Please try again.")
                continue
                
            # Try to open the file to check if it exists and is readable
            with open(input_filename, 'r', encoding='utf-8') as test_file:
                pass  # Just testing if we can open it
                
            break  # Exit loop if file is accessible
            
        except FileNotFoundError:
            print(f"❌ Error: File '{input_filename}' not found. Please check the filename.")
        except PermissionError:
            print(f"❌ Error: Permission denied to read '{input_filename}'.")
        except UnicodeDecodeError:
            print(f"❌ Error: Cannot decode file '{input_filename}'. It might be a binary file.")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
    
    # Get output filename
    while True:
        output_filename = input("Enter the output filename: ").strip()
        
        if not output_filename:
            print("❌ Error: Output filename cannot be empty.")
            continue
            
        if output_filename == input_filename:
            print("❌ Error: Output filename cannot be the same as input filename.")
            continue
            
        # Check if output file already exists
        try:
            with open(output_filename, 'r'):
                overwrite = input(f"⚠️  File '{output_filename}' already exists. Overwrite? (y/n): ").lower()
                if overwrite != 'y':
                    continue
        except FileNotFoundError:
            pass  # File doesn't exist, which is good
        except Exception as e:
            print(f"❌ Error checking output file: {e}")
            continue
            
        break
    
    # Process the file
    try:
        # Read the input file
        print(f"\n📖 Reading file: {input_filename}")
        with open(input_filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        print(f"✅ Successfully read {len(content)} characters")
        
        # Modify the content (you can customize this function)
        modified_content = modify_content(content)
        
        # Write to output file
        print(f"📝 Writing to file: {output_filename}")
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(modified_content)
        
        print(f"✅ Success! Modified content written to '{output_filename}'")
        print(f"📊 Original size: {len(content)} characters")
        print(f"📊 Modified size: {len(modified_content)} characters")
        
    except Exception as e:
        print(f"❌ Error during file processing: {e}")

def modify_content(content):
    """
    Modify the file content according to specific rules.
    Customize this function based on your needs.
    """
    # Example modifications - you can change these as needed
    modifications = [
        ("  ", " "),  # Replace double spaces with single space
        ("\n\n\n", "\n\n"),  # Replace triple newlines with double
        # Add more modification rules here
    ]
    
    modified = content
    
    # Apply all modifications
    for old, new in modifications:
        modified = modified.replace(old, new)
    
    # Add a header to indicate the file was processed
    header = f"/* Processed by File Processor - {len(modified)} characters */\n\n"
    modified = header + modified
    
    return modified

def display_file_info(filename):
    """
    Display information about a file (optional feature)
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        print(f"\n📊 File Information for '{filename}':")
        print(f"   Lines: {len(lines)}")
        print(f"   Characters: {sum(len(line) for line in lines)}")
        print(f"   Words: {sum(len(line.split()) for line in lines)}")
        
    except Exception as e:
        print(f"❌ Error getting file info: {e}")

# Main program execution
if __name__ == "__main__":
    try:
        file_processor()
        
        # Optional: Ask if user wants to see file info
        see_info = input("\nWould you like to see file information? (y/n): ").lower()
        if see_info == 'y':
            input_file = input("Enter filename to get info: ").strip()
            if input_file:
                display_file_info(input_file)
        
        print("\n🎉 Program completed successfully!")
        
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\n💥 Unexpected error in main program: {e}")