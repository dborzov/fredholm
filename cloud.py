from boto.ec2.connection import EC2Connection
conn = EC2Connection('AKIAI3ZQRPCVRCEKOVSQ', 'heM7tubtH4/PEp4FjUwKG0J7AzxwjdtKbMFvl3oJ')
conn.run_instances(
    'ami-e565ba8c',
    key_name='dima-ec2-key',
    instance_type='t1.micro',
    security_groups=['quick-start-1'])