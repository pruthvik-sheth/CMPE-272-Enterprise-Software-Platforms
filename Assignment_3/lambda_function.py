import json
import random
from PIL import Image, ImageDraw, ImageFont
import boto3
import base64
from io import BytesIO

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # List of doge image keys in S3
    doge_images = ["doge1.jpg", "doge2.jpg", "doge3.jpg", "doge4.jpg", "doge5.jpg"]
    
    # Randomly select a doge image
    selected_doge = random.choice(doge_images)
    
    # Load randomly selected base image
    response = s3.get_object(Bucket='doge-meme-generator', Key=selected_doge)
    image = Image.open(BytesIO(response['Body'].read()))
    
    # Prepare drawing context
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("/tmp/comic.ttf", 30)
    
    # List of doge phrases
    phrases = ["much wow", "so cool", "very nice", "such awesome", "many colors", "wow", "amaze"]
    
    # Add text to image
    for i in range(5):
        x = random.randint(10, image.width - 100)
        y = random.randint(10, image.height - 30)
        phrase = random.choice(phrases)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.text((x, y), phrase, font=font, fill=color)
    
    # Save image to buffer
    buffer = BytesIO()
    image.save(buffer, format="JPEG")
    buffer.seek(0)
    
    # Encode image to base64
    img_str = base64.b64encode(buffer.getvalue()).decode()
    
    return {
        'statusCode': 200,
        'body': json.dumps({'image': img_str}),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }