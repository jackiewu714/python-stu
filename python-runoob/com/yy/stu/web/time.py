from datetime import datetime;

msg = '''
    <html>
        <body>
            <p>Generated {0}</p>
        </body>
    </html>
''';

msg = msg.format(datetime.now());

print(msg);

print(type("123"));
print(isinstance("123", str));