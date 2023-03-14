import pulsar

client = pulsar.Client('pulsar://pulsar-release-proxy.pulsar.svc.cluster.local:6650')

producer = client.create_producer('topic-inicio-flujo-gestor-inventario')

producer.send('Iniciar flujo!'.encode('utf-8'))

client.close()