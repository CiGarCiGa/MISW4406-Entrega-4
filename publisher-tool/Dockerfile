FROM eclipse-temurin:17-jdk-alpine
EXPOSE 8083
VOLUME /tmp
COPY publisher-tool/build/libs/demo-0.0.1-SNAPSHOT.jar app.jar
ENTRYPOINT ["java","-jar","/app.jar","--add-opens","java.base/sun.net=ALL-UNNAMED","--add-opens","java.management/sun.management=ALL-UNNAMED"]