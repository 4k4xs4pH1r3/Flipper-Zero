#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>

int main(int argc, char *argv[]) {
  int fd;
  char buf[1024];
  int ret;

  fd = open("/sys/class/thermal/thermal_zone0/temp", O_RDONLY);
  if (fd < 0) {
    perror("open");
    return 1;
  }

  ret = read(fd, buf, sizeof(buf));
  if (ret < 0) {
    perror("read");
    return 1;
  }

  printf("Temperature: %d\n", atoi(buf));

  close(fd);

  return 0;
}
